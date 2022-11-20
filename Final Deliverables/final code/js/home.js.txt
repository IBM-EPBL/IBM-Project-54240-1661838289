const productcontainers = [...document.querySelectorAll('.product-container')];
const nxtbtn = [...document.querySelectorAll('.nxt-btn')];
const prebtn = [...document.querySelectorAll('.pre-btn')];

productcontainers.forEach((item, i) => {
    let containerDimenstions = item.getBoundingClientRect()
    let containerwidth = containerDimenstions.width;

    nxtbtn[i].addEventListener('click', () => {
        item.scrollLeft += containerwidth;

    })

    prebtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerwidth;
        
    })
})