jQuery(function ($) {

  /* Functions */
  var loadForm = function () {
    var btn = $(this);

    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      enctype: 'multipart/form-data',
      contentType: false,
      processData: false,
      beforeSend: function () {
        $("#modal-site .modal-content").html("");
        $("#modal-site").modal("show");
      },
      success: function (data) {
        $("#modal-site .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    var formData = new formData(this);
    console.log(formData);
    $.ajax({
      url: form.attr("action"),
      method: 'POST',
      // data: form.serialize(),
      data: formData,
      type: form.attr("method"),
      dataType: 'json',
      enctype: 'multipart/form-data',
      contentType: false,
      processData: false,
      success: function (data) {
        if (data.form_is_valid) {
          //alert(data)
          $("#site-table tbody").html(data.html_site_list);
          $("#modal-site").modal("hide");
        }
        else {
          $("#modal-site .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create site
  $(".js-create-site").click(loadForm);
  $("#modal-site").on("submit", ".js-site-create-form", saveForm);

  // Update site
  $("#site-table").on("click", ".js-update-site", loadForm);
  $("#modal-site").on("submit", ".js-site-update-form", saveForm);

  // Update password
  $("#site-table").on("click", ".js-site-update-password", loadForm);
  $("#modal-site").on("submit", "js-site-update-password", saveForm);

  // Delete site
  $("#site-table").on("click", ".js-delete-site", loadForm);
  $("#modal-site").on("submit", ".js-site-delete-form", saveForm);

});
