jQuery(function ($) {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-faq .modal-content").html("");
        $("#modal-faq").modal("show");
      },
      success: function (data) {
        $("#modal-faq .modal-content").html(data.html_form);
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
          $("#faq-table tbody").html(data.html_faq_list);
          $("#modal-faq").modal("hide");
        }
        else {
          $("#modal-faq .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create faq
  $(".js-create-faq").click(loadForm);
  $("#modal-faq").on("submit", ".js-faq-create-form", saveForm);

  // Update faq
  $("#faq-table").on("click", ".js-update-faq", loadForm);
  $("#modal-faq").on("submit", ".js-faq-update-form", saveForm);



  // Delete faq
  $("#faq-table").on("click", ".js-delete-faq", loadForm);
  $("#modal-faq").on("submit", ".js-faq-delete-form", saveForm);

});
