'use strict';

const openMenuMobile = document.querySelector('.open_sidebar_btn');
const closeMenuMobile = document.querySelector('.close_sidebar_btn');
const classMenuOpener = document.querySelector('.site');

const whereToSendPayment = document.getElementsByName('email_or_phone');
const sendToPhone = document.getElementById('send_request_to_phone');
const sendToEmail = document.getElementsByName('send_request_to_email');


whereToSendPayment.forEach((values, key) =>{
      values.addEventListener('change', ()=>{
            let t = document.querySelector('input[name="email_or_phone"]:checked').value;
            if(t === 'phone'){
                  console.log(t);
                  classMenuOpener.classList.add('showRecipientPhoneBox');
                  classMenuOpener.classList.remove('showRecipientEmailBox');
            } else if (t === "email"){
                  console.log(t);
                  classMenuOpener.classList.add('showRecipientEmailBox');
                  classMenuOpener.classList.remove('showRecipientPhoneBox');
            }
      });
})

openMenuMobile.addEventListener('click', ()=> {
      classMenuOpener.classList.add('openMobileMenu');
});
closeMenuMobile.addEventListener('click', ()=> {
      if(classMenuOpener.classList.contains('openMobileMenu')){
            classMenuOpener.classList.remove('openMobileMenu');
      }
});

const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
            if (entry.intersectionRatio > 0){
                  entry.target.classList.add('this');
            }
      })
})
const boxEllist = document.querySelectorAll('.animate');
boxEllist.forEach((el) => {
      io.observe(el);
})