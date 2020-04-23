$(function () {
    $('#sign_in').validate({
        rules: {
            email: {
                required: true
            },
            password: {
                required: true,
                minlength: 8
            }
        },
        messages: {
            email: {
                required: 'Por favor ingrese su email.',
                email: 'Por favor ingrese un email valido.'
            },
            password: {
                required: 'Por favor ingrese su contraseña.',
                minlength: 'La contraseña debe tener minimo 8 caracteres.'
            }
        },
        highlight: function (input) {
            $(input).addClass('is-invalid');
        },
        unhighlight: function (input) {
            $(input).removeClass('is-invalid');
        },
        errorPlacement: function (error, element) {
            $(element).parents('.form-group').append(error.addClass('invalid-feedback'));
        }
    });
});