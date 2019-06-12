jQuery(function ($) {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-real .modal-content").html("");
        $("#modal-real").modal("show");
      },
      success: function (data) {
        $("#modal-real .modal-content").html(data.html_form);
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
          $("#real-table tbody").html(data.html_real_list);
          $("#modal-real").modal("hide");
        }
        else {
          $("#modal-real .modal-content").html(data.html_form);
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

  // Create real
  $(".js-create-real").click(loadForm);
  $("#modal-real").on("submit", ".js-real-create-form", saveForm);

  // Update real
  $("#real-table").on("click", ".js-update-real", loadForm);
  $("#modal-real").on("submit", ".js-real-update-form", saveForm);

  // Delete real
  $("#real-table").on("click", ".js-delete-real", loadForm);
  $("#modal-real").on("submit", ".js-real-delete-form", saveForm);

});
