function create_cookie(cookies_info) {
    document.cookie = cookies_info;
};
function redirect_index() {
    this.location = "./home.html";
};
setTimeout(redirect_index, 500);
create_cookie(`Login ${true}`);