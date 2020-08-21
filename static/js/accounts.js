$(".add-account-btn").on("click", () => {
    modal = $("#addAccountModal");
    modal.modal("show");
})

$("#AH_CreateAccountForm").on("submit", (event) => {
    event.preventDefault();

    let formData = new FormData();
    let logo = $("#AH_AccountLogo")[0].files[0];

    formData.append('name', $("#AH_AccountName").val());
    formData.append('balance', $("#AH_AccountBalance").val());
    formData.append('logo', logo);
    $.ajax({
        url: "/accounts",
        type: "POST",
        data: formData,
        contentType: false,
        processData: false,
        success: (data) => {
            alert(data.message);
            window.location.reload();
        },
        error: (err) => {
            alert(err.responseJSON.message);
            window.location.reload();
        }
    })
});