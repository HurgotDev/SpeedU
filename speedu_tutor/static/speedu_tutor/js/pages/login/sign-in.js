$(function () {
    $('#sign_in').validate({
        rules: {
            username: {
                required: true,
                minlength: 4
            },
            password: {
                required: true,
                minlength: 8
            }
        },
        messages: {
            username: {
                required: 'Por favor ingrese su nombre de usuario.',
                minlength: 'El nombre de usuario debe tener minimo 4 caracteres.'
            },
            password: {
                required: 'Por favor ingrese su contraseña.',
                minlength: 'La contraseña debe tener minimo 8 caracteres.'
            }
        },
        highlight: function (input) {
           7// console.log(input);
            $(input).parents('.form-line').addClass('error');
        },
        unhighlight: function (input) {
            $(input).parents('.form-line').removeClass('error');
        },
        errorPlacement: function (error, element) {
            $(element).parents('.input-group').append(error);
        }
    });
});