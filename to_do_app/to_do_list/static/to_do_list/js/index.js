window.onload = function () {
    bootlint.showLintReportForCurrentDocument([], {
        hasProblems: false,
        problemFree: false
    });

    $('[data-toggle="tooltip"]').tooltip();

    function formatDate(date) {
        return (
            date.getDate() +
            "/" +
            (date.getMonth() + 1) +
            "/" +
            date.getFullYear()
        );
    }

    var currentDate = formatDate(new Date());

    $(".due-date-button").datepicker({
        format: "dd/mm/yyyy",
        autoclose: true,
        todayHighlight: true,
        startDate: currentDate,
        orientation: "bottom right"
    });

    $(".due-date-button").on("click", function (event) {
        $(".due-date-button")
            .datepicker("show")
            .on("changeDate", function (dateChangeEvent) {
                $(".due-date-button").datepicker("hide");
                $(".due-date-label").text(formatDate(dateChangeEvent.date));
            });
    });
};
const editButtons = document.querySelectorAll('.fa-pencil');

editButtons.forEach(button => {
  button.addEventListener('click', () => {
    const todoItem = button.closest('.todo-item');
    const inputField = todoItem.querySelector('.edit-todo-input');

    if (inputField.readOnly) {
      inputField.readOnly = false; // Снимаем атрибут readonly
    } else {
      inputField.readOnly = true; // Возвращаем атрибут readonly
    }
  });
});
