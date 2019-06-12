jQuery(function ($) {
    /* Functions */
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-monthly .modal-content").html("");
          $("#modal-monthly").modal("show");
        },
        success: function (data) {
          $("#modal-monthly .modal-content").html(data.html_form);
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
            $("#monthly-table tbody").html(data.html_monthly_list);
            $("#modal-monthly").modal("hide");
          }
          else {
            $("#modal-monthly .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };


    /* Binding */

    // Create monthly
    $(".js-create-monthly").click(loadForm);
    $("#modal-monthly").on("submit", ".js-monthly-create-form", saveForm);

    // Update monthly
    $("#monthly-table").on("click", ".js-update-monthly", loadForm);
    $("#modal-monthly").on("submit", ".js-monthly-update-form", saveForm);

    // Delete monthly
    $("#monthly-table").on("click", ".js-delete-monthly", loadForm);
    $("#modal-monthly").on("submit", ".js-monthly-delete-form", saveForm);

  });
