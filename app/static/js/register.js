
// form step in the admin dashboard and in the register page

const nextButton = document.querySelector(".btn-next");
const prevButton = document.querySelector(".btn-prev");
const steps = document.querySelectorAll(".step");
const form_steps = document.querySelectorAll(".form_step");

let active = 1;
nextButton.addEventListener("click", () => {
    active++;
//     console.log(form_steps.length);
    if(active > form_steps.length){
        active = form_steps.length;
    }
    updateProgress();
});

prevButton.addEventListener("click", () => {
    active--;
    if(active < 1){
        active = 1;
    }
    updateProgress();
});
function updateProgress() {

    // toggle active class for each item

    form_steps.forEach((step, i) => {
        if (i == (active-1)) {
            form_steps[i].classList.add('active');
        } else {
            form_steps[i].classList.remove('active');
        }
    });
    
    //enable to disable prev and next button
    if (active === 1){
        prevButton.disabled = true;
    } else if (active === steps.length) {
        nextButton.disabled = true;
    } else{
        prevButton.disabled = false;
        nextButton.disabled = false;
    }
}