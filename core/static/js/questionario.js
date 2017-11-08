function autoRefresh(interval) {
    setTimeout("atualizar();",interval);
}
function atualizar() {
    alert("Tempo Esgotado");
    document.getElementById("id_formulario").click();
}