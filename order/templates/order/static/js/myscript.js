$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    console.log("ID", id)
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data:{
            prod_id: id
        },
        success: function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    // console.log("ID", id)
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data:{
            prod_id: id
        },
        success: function(data){
            console.log("Q", data.quantity)
            if (data.quantity !== undefined){
                console.log('enter if');
                eml.innerText = data.quantity
                document.getElementById("amount").innerText = data.amount
                document.getElementById("totalamount").innerText = data.totalamount     
            }else{
                console.log('else');
                window.location.href='/cart';
            }
            
        }
    })
})

$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this
    console.log("ID", id)
    $.ajax({
        type: "GET",
        url: "/removecart",
        data:{
            prod_id: id
        },
        success: function(data){
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount    
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            // window.location.href='/cart'

        }
    })
})