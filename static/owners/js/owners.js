jQuery(function ($) {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-owner .modal-content").html("");
        $("#modal-owner").modal("show");
      },
      success: function (data) {
        $("#modal-owner .modal-content").html(data.html_form);
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
          $("#owner-table tbody").html(data.html_owner_list);
          $("#modal-owner").modal("hide");
        }
        else {
          $("#modal-owner .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create owner
  $(".js-create-owner").click(loadForm);
  $("#modal-owner").on("submit", ".js-owner-create-form", saveForm);

  // Update owner
  $("#owner-table").on("click", ".js-update-owner", loadForm);
  $("#modal-owner").on("submit", ".js-owner-update-form", saveForm);



  // Delete owner
  $("#owner-table").on("click", ".js-delete-owner", loadForm);
  $("#modal-owner").on("submit", ".js-owner-delete-form", saveForm);

});
