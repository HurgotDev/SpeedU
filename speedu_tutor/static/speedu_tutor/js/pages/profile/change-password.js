$(function () {
    $('#form_change_password').validate({
        rules: {
            current_password: {
                required: true,
                minlength: 8
            },
            new_password: {
                required: true,
                minlength: 8
            },
            confirm_password: {
                required: true,
                equalTo: new_password,
                minlength: 8
            }
        },
        messages: {
            current_password: {
                required: 'Por favor ingrese su contraseña actual.',
                minlength: 'La contraseña debe tener minimo 8 caracteres.'
            },
            new_password: {
                required: 'Por favor ingrese su nueva contraseña.',
                minlength: 'La contraseña debe tener minimo 8 caracteres.'
            },
            confirm_password: {
                required: 'Por favor confirme su contraseña.',
                equalTo: 'Las contraseñas no coinciden.',
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