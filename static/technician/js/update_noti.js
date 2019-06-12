jQuery(function ($) {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-noti .modal-content").html("");
        $("#modal-noti").modal("show");
      },
      success: function (data) {
        $("#modal-noti .modal-content").html(data.html_form);
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
          $("#noti-table tbody").html(data.html_noti_list);
          $("#modal-noti").modal("hide");
        }
        else {
          $("#modal-noti .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create noti
  $(".js-create-noti").click(loadForm);
  $("#modal-noti").on("submit", ".js-noti-create-form", saveForm);

  // Update noti
  $("#noti-table").on("click", ".js-update-noti", loadForm);
  $("#modal-noti").on("submit", ".js-noti-update-form", saveForm);

  // Delete noti
  $("#noti-table").on("click", ".js-delete-noti", loadForm);
  $("#modal-noti").on("submit", ".js-noti-delete-form", saveForm);

});
