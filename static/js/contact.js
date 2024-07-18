
function init() {
    console.log("Contact  page!!!!")

    const templateId = "template_m9nv57u";

    const publicKey = "XTclsZaqwqg6x6pUu";

    const serviceId = "service_aw5uvzt";

    emailjs.init(publicKey);

    document.getElementById("contactForm").addEventListener("submit", function(event) {
        event.preventDefault();

        const form = event.target;
        const name = form.elements.name.vale;
        const email = form.elements.email.value;
        const message = form.elements.message.value;

        const params = {
            name,
            email,
            message
        }


        emailjs.send(serviceId, templateId, params).then(
            (res) => {
              alert('message sent');
            },
            (error) => {
              console.log(error);
              alert('Error sending email 🥺');
            }
          );
    
    });

       

}

window.onload = init;