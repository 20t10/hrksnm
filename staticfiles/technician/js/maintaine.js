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
        $("#modal-maintaine .modal-content").html("");
        $("#modal-maintaine").modal("show");
      },
      success: function (data) {
        $("#modal-maintaine .modal-content").html(data.html_form);
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
      data: formData,
      type: form.attr("method"),
      dataType: 'json',
      enctype: 'multipart/form-data',
      contentType: false,
      processData: false,
      success: function (data) {
        if (data.form_is_valid) {
          //alert(data)
          $("#maintaine-table tbody").html(data.html_maintaine_list);
          $("#modal-maintaine").modal("hide");
        }
        else {
          $("#modal-maintaine .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create maintaine
  $(".js-create-maintaine").click(loadForm);
  $("#modal-maintaine").on("submit", ".js-maintaine-create-form", saveForm);

  // Update maintaine
  $("#maintaine-table").on("click", ".js-update-maintaine", loadForm);
  $("#modal-maintaine").on("submit", ".js-maintaine-update-form", saveForm);

  // Delete maintaine
  $("#maintaine-table").on("click", ".js-delete-maintaine", loadForm);
  $("#modal-maintaine").on("submit", ".js-maintaine-delete-form", saveForm);

});
