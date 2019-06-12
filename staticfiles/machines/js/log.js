jQuery(function ($) {
  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-log .modal-content").html("");
        $("#modal-log").modal("show");
      },
      success: function (data) {
        $("#modal-log .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#log-table tbody").html(data.html_log_list);
          $("#modal-log").modal("hide");
        }
        else {
          $("#modal-log .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };





  // $(document).ready(function ($) {
  //   refresh();
  //   var int = setInterval("refresh()", 1000);
  // };

  /* Binding */
  $('.js-refresh-page').click(function() {
      window.location.href=window.location.href;
  });

  // Create log
  $(".js-create-log").click(loadForm);
  $("#modal-log").on("submit", ".js-log-create-form", saveForm);

  // Update log
  $("#log-table").on("click", ".js-update-log", loadForm);
  $("#modal-log").on("submit", ".js-log-update-form", saveForm);

  // Delete log
  $("#log-table").on("click", ".js-delete-log", loadForm);
  $("#modal-log").on("submit", ".js-log-delete-form", saveForm);

});
