$(document).ready(function () {
    // Highlight form fields on focus
    $("input[type='text'], input[type='number'], input[type='date']").focus(function () {
        $(this).css("border-color", "#3498db");
    }).blur(function () {
        $(this).css("border-color", "#dcdde1");
    });

    // Show an alert on form submission
    $("form").submit(function (event) {
        alert("¡Formulario enviado exitosamente!");
    });
});
