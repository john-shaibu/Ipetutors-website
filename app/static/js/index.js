const menuTrigger = document.querySelector('.menu-trigger');
const closeTrigger = document.querySelector('.close');
const giveClass = document.querySelector('.site');


menuTrigger.addEventListener('click', function(){
      giveClass.classList.toggle('showMenu');
});

closeTrigger.addEventListener('click',function(){
      giveClass.classList.remove('showMenu');
});

const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
            if (entry.intersectionRatio > 0){
                  entry.target.classList.add('this')
            }
      })
})
const boxEllist = document.querySelectorAll('.animate');
boxEllist.forEach((el) => {
      io.observe(el);
})




document.addEventListener('scroll', ()=> {
      // const header = document.getElementsByTagName('header');
      console.log('activated');

      if (window.scrollY > 70){
            console.log('greater than zero');
            giveClass.classList.add('show-header');
      } else{
            giveClass.classList.remove('show-header');
      }
});


// THE CODE HERE WORKS FOR THE REGISTER POPUP

const closeRegisterPopup = document.querySelector('.close_popup_btn');
const openRegisterPopup = document.querySelector('.open_register_btn');

openRegisterPopup.addEventListener('click', ()=>{
      console.log('shown')
      giveClass.classList.add('openReg_Popup');
})
closeRegisterPopup.addEventListener('click', ()=>{
      giveClass.classList.remove('openReg_Popup');
})

// the code here changes th testimonial  section
// const slideIndex = 0;
// showSlides();

// function showSlides() {
//       let i;
//       let slides = document.getElementsByClassName("testimonials-inner");
//       let dots = document.getElementsByClassName("dots");
//       for (i = 0; i < slides.length; i++) {
//             slides[i].style.display = "none";  
//       }
//       slideIndex++;
//       if (slideIndex > slides.length) {slideIndex = 1}    
//       for (i = 0; i < dots.length; i++) {
//             dots[i].className = dots[i].className.replace(" active", "");
//       }
//       slides[slideIndex-1].style.display = "block";  
//       dots[slideIndex-1].className += " active";
//       setTimeout(showSlides, 5000); // Change image every 2 seconds
// }