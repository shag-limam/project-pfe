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
            TypeDemande: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            denomination: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            siege: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            numIMM: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            nomPrenom: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            Nationalite: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            lieu_nais: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            cnss: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            numPass: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            dateExpPass: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            email: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            numTel: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            dateNaissance: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            descPoste: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                alphanumeric: true
            },
            expose: {
                required: true,
                noSpace: true
            },
            photo: {
                required: true,
                noSpace: true
            },
            gender: {
                required: true
            },
            hobbies: {
                required: true
            },
            TypePermis: {
                required: true
            },

        },
        messages: {
            TypeDemande: {
                required: "selectionne le type de demande s'il vous plait ! "
            },
            denomination: {
                //error message for the required field
                required: 'saisir un denomination ! '
            },
            siege: {
                //error message for the required field
                required: 'saisir un siege valide ! '
            },
            numIMM: {
                //error message for the required field
                required: "saisir un numIMM valide ! "
            },
            nomPrenom: {
                //error message for the required field
                required: 'saisir un numero du telephone valide ! '
            },
            Nationalite: {
                required: "selectionne une Nationalite s'il vous plait ! "
            },
            lieu_nais: {
                //error message for the required field
                required: 'saisir votr tieux de naissance ! '
            },
            cnss: {
                //error message for the required field
                required: 'saisir un cnss! '
            },
            numPass: {
                //error message for the required field
                required: "saisir un numero du  pasport ! "
            },
            dateExpPass: {
                //error message for the required field
                required: 'saisir le nom valide ! '
            },
            email: {
                //error message for the required field
                required: 'saisir un gmail ! ',

                //error message for the email field
                email: "s'il vous plait saisir un gmail valide !"
            },

            numTel: {
                //error message for the required field
                required: 'saisir un numero du telephone valide ! '
            },
            dateNaissance: {
                //error message for the required field
                required: 'saisir un date de naissance valide ! '
            },
            descPoste: {
                //error message for the required field
                required: "saisir une description du post valide ! "
            },
            expose: {
                required: "charger une photo du pasport s'il vous plait!"
            },
            photo: {
                required: "charger votr image s'il vous plait!"
            },
            region: {
                required: "selectionne une region s'il vous plait ! "
            },
            TypePermis: {
                required: "selectionne le type du permis s'il vous plait ! "
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