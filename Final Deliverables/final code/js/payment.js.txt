

//  1.....................................Deliveery options......................................................//

let homeDelivery =document.getElementById("home-delivery").addEventListener("click",HomeDelivery)
 homeDelivery =document.getElementById("home-delivery").style.border="2px solid orange"

// const api_key="07a51eea324d30f39c87a220dc518de8";

function HomeDelivery(){
    
    window.location.reload();
    
}

// 2.............................................Search City By Input..........................................................................//





let storeDelivery= document.getElementById("store-delivery").addEventListener("click",StoreDelivery)

function StoreDelivery(){
   let HideDiv1=document.getElementById("delivery-info").style.display="none";
   let HideDiv2=document.getElementById("location-info").style.display="block";
   let input_tag=document.getElementById("city_search").style.display="block";
   
   let homeDelivery =document.getElementById("home-delivery").style.border="1px solid #bdc6ce";
   let storeDelivery= document.getElementById("store-delivery").style.border="2px solid orange";

   let count=3;
    let id=setInterval(function(){
        let iframe=document.getElementById("gmap_canvas");
        iframe.src="https://flevix.com/wp-content/uploads/2019/07/Curve-Loading.gif"
    count--;
    if(count===0){
    clearInterval(id);
    let iframe=document.getElementById("gmap_canvas");
    iframe.src=`https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.1661668426377!2d80.03171181475606!3d13.02508819082081!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a528b0aff5ff8ff%3A0x9ccd29ac00bf26b5!2sLoyola%20Institute%20of%20Technology!5e0!3m2!1sen!2sin!4v1668444898761!5m2!1sen!2sin" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade` 
}
},1000);
   


   let city=document.getElementById("city").addEventListener("oninput",ShowMap)
   function ShowMap(){
    let city=document.getElementById("city").value;
    console.log(city)
   }
}

//  3...................................................Debit And Credit Card Div.....................................................................//

let debitCard=document.getElementById("debit-card").addEventListener("dblclick",DebitCard)
function DebitCard(){
    let card_details=document.querySelector("#card-details")
    if(card_details.style.display==="none")
    {
        card_details.style.display="block";
    }
    else{
        card_details.style.display="none"
    }
}

//  4........................................................EMI div.........................................................

let EMI=document.getElementById("emi").addEventListener("dblclick",Emi)
function Emi(){
    let card_details=document.querySelector("#emi-card-1")
    if(card_details.style.display==="none")
    {
        card_details.style.display="block";
    }
    else{
        card_details.style.display="none"
    }
}


//  5.............................................................Net Banking-div......................................................................//

let netBank=document.getElementById("net-bank").addEventListener("dblclick",NetBank)
function NetBank(){
    let card_details=document.querySelector("#net-banking-div")
    if(card_details.style.display==="none")
    {
        card_details.style.display="block";
    }
    else{
        card_details.style.display="none"
    }
}

//  6...........................................................Wallet-div..............................................................................//

let Wallet =document.getElementById("wallets").addEventListener("dblclick",WalletInput)

function WalletInput(){
    let card_details=document.querySelector("#wallet-div")
    if(card_details.style.display==="none")
    {
        card_details.style.display="block";
    }
    else{
        card_details.style.display="none"
    }
}

    let Wallet_input =document.getElementById("select-wallet").addEventListener("click",WalletOpt)
    function WalletOpt(){
    let card_details=document.querySelector("#wallet-div-info")
    if(card_details.style.display==="none")
    {
        card_details.style.display="block";
    }
    else{
        card_details.style.display="none"
    }

}


// 7. ............................................................UPI..................................................../......................

let UPI_pay=document.getElementById("upi").addEventListener("dblclick",upi_Pay)
function upi_Pay(){
    let card_details=document.querySelector("#Upi-Opt")
    if(card_details.style.display==="none")
    {
        card_details.style.display="block";
    }
    else{
        card_details.style.display="none"
    }
}



//.7..............................for input tag.........................................................................//

let button_show=document.getElementById("pay-now").addEventListener("click",ShowStatus)

function ShowStatus(){
let UserArray=[]
    let userData=document.getElementById("user-form-datails")
    
    let UserData={
        Uname:userData.user_name.value,
        flat:userData.user_flat.value,
        buildingName:userData.user_building_name.value,
        City:userData.user_city.value,
        state:userData.user_state.value,
        pincode:userData.user_pin_cd.value,
        contactNo:userData.user_contact.value,
        
    }
    UserArray.push(UserData)

    console.log(UserArray[0].Uname)

    let check_inform=document.getElementById("final-confirmation")

    let h2=document.createElement("h2");
    h2.innerText="Please confirmed Below details";

    let name=document.createElement("p")
    name.innerText=`Name:${UserArray[0].Uname}`

    let contact=document.createElement("p")
    contact.innerText=`Contact No:${UserArray[0].contactNo}`;
   

    let pincode=document.createElement("p")
    pincode.innerText=`Pincode No.:${UserArray[0].pincode}`

    let city=document.createElement("p")
    city.innerText=`City:${UserArray[0].City}`

    let state=document.createElement("p")
    state.innerText=`State:${UserArray[0].state}`

    let buildingname=document.createElement("p")
    buildingname.innerText=`Building Name:${UserArray[0].buildingName}`

    let flat=document.createElement("p")
    flat.innerText=`Flat No.:${UserArray[0].flat}`

    let not4=document.createElement("h2")
        not4.innerText=`Payable Amount :₹${subtotal}`
    
    let com_btn=document.createElement("button")
    com_btn.id="checck_info"
    com_btn.innerText="Conform"
    com_btn.addEventListener("click",Csheck_Info)

    console.log(h2,name,flat,buildingname,city,state,pincode,contact,not4)

    let div_show =document.getElementById("out-put")
    div_show.style.display="block"

    check_inform.append(h2,name,flat,buildingname,city,state,pincode,contact,not4,com_btn)
    div_show.append(check_inform)
    
//8............................................button Event.............................................................//

    function Csheck_Info(){
    let check_inform=document.getElementById("final-confirmation")
    check_inform.style.display="none"

    let time =document.getElementById("order-process");
    time.style.display="block"

    let note_1=document.getElementById("note-1")
    note_1.innerText=`Thanks you ${UserArray[0].Uname} for Shoping with us. Your Order confirmation is pending`

 
    let count=5;
    let id=setInterval(function(){
    count--;
    if(count===0){
    clearInterval(id);
    let time =document.getElementById("order-process");
    time.style.display="none"
    let div_show =document.getElementById("order-placed")
    div_show.style.display="block"
    let note_2=document.getElementById("note-2")
    note_2.innerText=`Congratualtions ${UserArray[0].Uname} Your order has been placed succesfully`
}
},1000);

let more_shop=document.getElementById("more-shop").addEventListener("click",moreShop)
function moreShop(){

   window.location.href="index.html";
   window.location.href="index.html"

} 
}

}

//................................. Data Append to ..........................................................................//

let Summary=JSON.parse(localStorage.getItem("checkout"));
let n=Summary[Summary.length-1]

let summary=(n)=>{

  n.forEach(function(ele,i){

    let summ_div = document.getElementById("append-basket");

    let prod_div = document.createElement("div");
    prod_div.setAttribute("id", "prod_div");

    let img_div = document.createElement("div");
    img_div.setAttribute("id", "div-img");

    let img = document.createElement("img");
    img.src = ele.img;

    let info_div = document.createElement("div");
    info_div.setAttribute("id", "info_div");

    let main_t=document.createElement("p")
    main_t.id="main_t"
    main_t.innerText="LIFESTYLE"

    let tit = document.createElement("p");
    tit.innerText = ele.productName;


    let m_div = document.createElement("div");
    m_div.setAttribute("id", "middle-div");


    let _quan = document.createElement("div");
    _quan.setAttribute("id", "quants");

    let quant=document.createElement("p")
    quant.innerText=`Qty:${1}`

    let price = document.createElement("p");
    price.id="price_tag"
    price.innerText =`Price: ₹${ele.price}`;

    _quan.append(quant)
    m_div.append(_quan,price)
    info_div.append(main_t,tit,m_div)
    img_div.append(img)
    prod_div.append(img_div,info_div)
    summ_div.append(prod_div)
  })
}
summary(n);

let subtotal = n.reduce(function (acc, ele) {
    return Math.round(acc + ele.price);
}, 0);

let SubTotal =subtotal+40

let total_price=document.getElementById("sub_total")
total_price.innerText=`₹${subtotal}`

 if(subtotal<999){
    let total_p=document.getElementById("total_cost")
    total_p.innerText=`₹${SubTotal}`
    let deli_charge=document.getElementById("deli_charge")
    deli_charge.innerText=`₹${40}`
   }else{
    let total_p=document.getElementById("total_cost")
     total_p.innerText=`₹${subtotal}`
     let deli_charge=document.getElementById("deli_charge")
    deli_charge.innerText="Free"
   }

// ......................Continue Last Pay Now Button....................................................................

// let bank_conf=document.getElementById("bank_conf")
// let not3=document.getElementById("u_details")
// not3.innerText=`${UserArray[0].Uname} Please Conform Your Order Payment`
// let not4=document.getElementById("amt_com")
// not4.innerText=`₹ ${subtotal}`
// let sub=document.getElementById("amt-pay").addEventListener("click",paymentComfirm)


// payment logo

let pay_logo_home=document.getElementById("payment-logo").addEventListener("click",HomePeJao)

function HomePeJao(){
    window.location.href="index.html";
   window.location.href="index.html"
}