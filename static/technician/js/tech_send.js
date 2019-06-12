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
          $("#modal-work .modal-content").html("");
          $("#modal-work").modal("show");
        },
        success: function (data) {
          $("#modal-work .modal-content").html(data.html_form);
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
            $("#work-table tbody").html(data.html_todo_list);
            $("#modal-work").modal("hide");
          }
          else {
            $("#modal-work .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create work
    $(".js-create-work").click(loadForm);
    $("#modal-work").on("submit", ".js-work-create-form", saveForm);
  
    // Update work
    $("#work-table").on("click", ".js-update-work", loadForm);
    $("#modal-work").on("submit", ".js-work-update-form", saveForm);
  
    // Delete work
    $("#work-table").on("click", ".js-delete-work", loadForm);
    $("#modal-work").on("submit", ".js-work-delete-form", saveForm);
  
  });
  