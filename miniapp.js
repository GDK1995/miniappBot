document.addEventListener("DOMContentLoaded", () => {
    const tg = window.Telegram.WebApp;
    tg.ready();

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

      const jsonData = JSON.stringify(data);

      if (jsonData.length === 0) {
        tg.showAlert('Данные пустые!');
        return;
      }

      if (new TextEncoder().encode(jsonData).length > 4096) {
        tg.showAlert('Данные слишком большие (более 4096 байт)');
        return;
      }

      try {
        tg.sendData(jsonData);
      } catch (e) {
        tg.showAlert(e.message);
      }
    });
})
