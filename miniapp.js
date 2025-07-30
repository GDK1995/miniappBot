const tg = window.Telegram.WebApp;

const regBtn = document.getElementById('register-btn');
const nameText = document.getElementById('name-text');
const dateText = document.getElementById('date-text');
const phoneText = document.getElementById('phone-text');
const emailText = document.getElementById('email-text');
const passwordText = document.getElementById('password-text');

regBtn.addEventListener("click", () => {
  const data = {
    first_name: nameText.value,
    host: "https://edu.excourse.kz/user-registrate",
    birth_date: dateText.value,
    email: emailText.value,
    last_name: "",
    password: passwordText.value,
    phone: phoneText.value,
    utmContent: "",
    utmSource: "",
    utmMedium: "",
    utmTerm: "",
    utmCampaign: ""
  };
  tg.sendData(JSON.stringify(data));
  console.log('>', JSON.stringify(data))
});

regBtn.addEventListener("touch", () => {
  tg.sendData(JSON.stringify(data));
});