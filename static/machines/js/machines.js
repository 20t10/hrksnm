jQuery(function ($) {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-machine .modal-content").html("");
        $("#modal-machine").modal("show");
      },
      success: function (data) {
        $("#modal-machine .modal-content").html(data.html_form);
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
          $("#machine-table tbody").html(data.html_machine_list);
          $("#modal-machine").modal("hide");
        }
        else {
          $("#modal-machine .modal-content").html(data.html_form);
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

  // Create machine
  $(".js-create-machine").click(loadForm);
  $("#modal-machine").on("submit", ".js-machine-create-form", saveForm);

  // Update machine
  $("#machine-table").on("click", ".js-update-machine", loadForm);
  $("#modal-machine").on("submit", ".js-machine-update-form", saveForm);

  // Delete machine
  $("#machine-table").on("click", ".js-delete-machine", loadForm);
  $("#modal-machine").on("submit", ".js-machine-delete-form", saveForm);

});
