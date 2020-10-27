// Find out the cart items from localStorage
if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
    updateCart(cart);
}

function updateCart(cart) {
    var sum = 0;
    for (var item in cart) {
        sum = sum + cart[item];
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
}

// If the add to cart button is clicked, add/increment the item
$('.cart').click(function () {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
        cart[idstr] = cart[idstr] + 1;
    } else {
        cart[idstr] = 1;
    }
    updateCart(cart);

});