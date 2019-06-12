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
        $("#modal-branch .modal-content").html("");
        $("#modal-branch").modal("show");
      },
      success: function (data) {
        $("#modal-branch .modal-content").html(data.html_form);
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
          $("#branch-table tbody").html(data.html_branch_list);
          $("#modal-branch").modal("hide");
        }
        else {
          $("#modal-branch .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create branch
  $(".js-create-branch").click(loadForm);
  $("#modal-branch").on("submit", ".js-branch-create-form", saveForm);

  // Update branch
  $("#branch-table").on("click", ".js-update-branch", loadForm);
  $("#modal-branch").on("submit", ".js-branch-update-form", saveForm);

  // Delete branch
  $("#branch-table").on("click", ".js-delete-branch", loadForm);
  $("#modal-branch").on("submit", ".js-branch-delete-form", saveForm);

});
