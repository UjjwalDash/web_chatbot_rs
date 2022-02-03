
function getBotResponse(input) {
    $.ajax({
        type: "GET",
        url: "/office",
        //dataType: "json",
        data: input,
        success : success_function
    });
    return 1;
}
function success_function(response) {

    // unpack response:
    let ans = response.key2;

    let botHtml = '<p class="botText"><span>' + ans + '</span></p>';
    $("#chatbox").append(botHtml);

    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}