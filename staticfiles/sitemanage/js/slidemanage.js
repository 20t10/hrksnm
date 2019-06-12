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
        $("#modal-slide .modal-content").html("");
        $("#modal-slide").modal("show");
      },
      success: function (data) {
        $("#modal-slide .modal-content").html(data.html_form);
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
          $("#slide-table tbody").html(data.html_slide_list);
          $("#modal-slide").modal("hide");
        }
        else {
          $("#modal-slide .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  $(".js-create-slide").click(loadForm);
  $("#modal-slide").on("submit", ".js-slide-create-form", saveForm);


  $("#slide-table").on("click", ".js-update-slide", loadForm);
  $("#modal-slide").on("submit", ".js-slide-update-form", saveForm);


  $("#slide-table").on("click", ".js-slide-update-password", loadForm);
  $("#modal-slide").on("submit", "js-slide-update-password", saveForm);


  $("#slide-table").on("click", ".js-delete-slide", loadForm);
  $("#modal-slide").on("submit", ".js-slide-delete-form", saveForm);

});
