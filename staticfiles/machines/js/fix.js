jQuery(function ($) {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-fix .modal-content").html("");
        $("#modal-fix").modal("show");
      },
      success: function (data) {
        $("#modal-fix .modal-content").html(data.html_form);
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
          $("#fix-table tbody").html(data.html_machine_list);
          $("#modal-fix").modal("hide");
        }
        else {
          $("#modal-fix .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Update fix
  $("#fix-table").on("click", ".js-update-fix", loadForm);
  $("#modal-fix").on("submit", ".js-fix-update-form", saveForm);

  // Delete fix
  $("#fix-table").on("click", ".js-delete-fix", loadForm);
  $("#modal-fix").on("submit", ".js-fix-delete-form", saveForm);

});
