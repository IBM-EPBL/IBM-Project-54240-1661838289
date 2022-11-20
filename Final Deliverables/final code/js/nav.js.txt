const creatNav = () => {
    let nav = document.querySelector('.navbar');

    nav.innerHTML = `
    <div class="nav">
    <img src="https://jaga2002.s3.jp-tok.cloud-object-storage.appdomain.cloud/logo.svg" class="brand-logo" alt="">
   <div class="nav-items">
          <div class="search">
              <input type="text" class="search-box" placeholder="search brand, product">
              <button class="search-btn">search</button>

               </div>
               
                 <a href="dashboard.html"><img src="https://jaga2002.s3.jp-tok.cloud-object-storage.appdomain.cloud/person-circle-outline.svg" alt=""></a>
                 <a href="cart.html"><img src="https://jaga2002.s3.jp-tok.cloud-object-storage.appdomain.cloud/cart-outline.svg" alt=""></a>
                 <a href="#"><img src="https://jaga2002.s3.jp-tok.cloud-object-storage.appdomain.cloud/heart-circle-outline.svg" alt=""></a>
                 <a href="signin.html" class="hello" >HELLO,SIGNIN</a>
                 <a href="adminsignin.html" class="admin"><img src="https://jaga2002.s3.jp-tok.cloud-object-storage.appdomain.cloud/person-circle-outline.svg"><span>Admin</span></a>
               
               </div>
               

</div>

<ul class="link-containers">

<li class="link-item"><a href="index.html" class="link">home</a></li>
<li class="link-item"><a href="women.html" class="link">women</a></li>
<li class="link-item"><a href="men.html" class="link">men</a></li>
<li class="link-item"><a href="kids.html" class="link">kids</a></li>
<li class="link-item"><a href="acessories.html" class="link">acessories</a></li> 


</ul>

    `;
}       
          
 creatNav();
