jQuery.validator.addMethod("noSpace", function(value, element) {
    return value == '' || value.trim().length != 0;
}, "No space please and don't leave it empty");
jQuery.validator.addMethod("customEmail", function(value, element) {
    return this.optional(element) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(value);
}, "Please enter valid email address!");
$.validator.addMethod("alphanumeric", function(value, element) {
    return this.optional(element) || /^\w+$/i.test(value);
}, "Letters, numbers, and underscores only please");
var $registrationForm = $('#registration');
if ($registrationForm.length) {
    $registrationForm.validate({
        rules: {
            //username is the name of the textbox
            Nom: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            siege: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            adresse: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            secteurActivite: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            FormeJuridique: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            email: {
                required: true,
                customEmail: true
            },
            gmail: {
                required: true,
                customEmail: true
            },
            password1: {
                required: true
            },
            password2: {
                required: true,
                equalTo: '#password'
            },
            NumeroCNSS: {
                required: true,
                noSpace: true
            },
            NumeroRC: {
                required: true,
                noSpace: true
            },
            gender: {
                required: true
            },
            hobbies: {
                required: true
            },
            region: {
                required: true
            },

        },
        messages: {
            Nom: {
                //error message for the required field
                required: 'saisir un nom valide ! '
            },
            siege: {
                //error message for the required field
                required: 'saisir un denomination valide ! '
            },
            adresse: {
                //error message for the required field
                required: 'saisir un adresse valide ! '
            },
            FormeJuridique: {
                //error message for the required field
                required: 'saisir un Forme Juridique valide ! '
            },
            secteurActivite: {
                //error message for the required field
                required: "saisir un Secteur d'activite valide ! "
            },
            email: {
                required: 'saisir un email valide ! ',
                //error message for the email field
                email: "s'il vous plait saisir un email valide"
            },
            gmail: {
                required: 'saisir un gmail valide ! ',
                //error message for the email field
                email: "s'il vous plait saisir un email valide !"
            },
            password1: {
                required: 'saisir un Mots de pass valide ! '
            },
            password2: {
                required: "saisir un Mots de pass ! ",
                equalTo: 'saisir le meme Mots de pass ci-dessou ! '
            },
            NumeroCNSS: {
                required: "charger une photo s'il vous plait!"
            },
            NumeroRC: {
                required: "charger une photo s'il vous plait!"
            },
            region: {
                required: "selectionne une region s'il vous plait ! "
            },

        },
        errorPlacement: function(error, element) {
            if (element.is(":radio")) {
                error.appendTo(element.parents('.gender'));
            } else if (element.is(":checkbox")) {
                error.appendTo(element.parents('.hobbies'));
            } else {
                error.insertAfter(element);
            }

        }
    });
}