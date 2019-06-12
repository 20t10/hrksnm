jQuery(function ($) {
    /* Functions */
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-withdraw .modal-content").html("");
          $("#modal-withdraw").modal("show");
        },
        success: function (data) {
          $("#modal-withdraw .modal-content").html(data.html_form);
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
            $("#withdraw-table tbody").html(data.html_withdraw_list);
            $("#modal-withdraw").modal("hide");
          }
          else {
            $("#modal-withdraw .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };


    /* Binding */

    // Create withdraw
    $(".js-create-withdraw").click(loadForm);
    $("#modal-withdraw").on("submit", ".js-withdraw-create-form", saveForm);

    // Update withdraw
    $("#withdraw-table").on("click", ".js-update-withdraw", loadForm);
    $("#modal-withdraw").on("submit", ".js-withdraw-update-form", saveForm);

    // Delete withdraw
    $("#withdraw-table").on("click", ".js-delete-withdraw", loadForm);
    $("#modal-withdraw").on("submit", ".js-withdraw-delete-form", saveForm);

  });
