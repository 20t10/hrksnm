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
        $("#modal-todo .modal-content").html("");
        $("#modal-todo").modal("show");
      },
      success: function (data) {
        $("#modal-todo .modal-content").html(data.html_form);
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
          $("#todo-table tbody").html(data.html_todo_list);
          $("#modal-todo").modal("hide");
        }
        else {
          $("#modal-todo .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create todo
  $(".js-create-todo").click(loadForm);
  $("#modal-todo").on("submit", ".js-todo-create-form", saveForm);

  // Update todo
  $("#todo-table").on("click", ".js-update-todo", loadForm);
  $("#modal-todo").on("submit", ".js-todo-update-form", saveForm);

  // Delete todo
  $("#todo-table").on("click", ".js-delete-todo", loadForm);
  $("#modal-todo").on("submit", ".js-todo-delete-form", saveForm);

});
