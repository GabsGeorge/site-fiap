function autoRefresh(interval) {
    setTimeout("atualizar();",interval);
}
function atualizar() {
    alert("Tempo Esgotado");
    // document.getElementById("id_formulario").click();
    // Tentei armazenar no banco usando Submit do Formulário, porem nao obtive sucesso
    Enviar();
}

function Enviar(){
    var resposta1 = document.getElementById("resposta1").value;
    var resposta2 = document.getElementById("resposta2").value;
    var resposta3 = document.getElementById("resposta3").value;
    var resposta4 = document.getElementById("correta_4").checked;
    var resposta5 = document.getElementById("correta_5").checked;
    var resposta6 = document.getElementById("correta_6").checked;
    var resposta7 = document.getElementById("correta_7").checked;
    var resposta8A = document.getElementById("correta_8A").checked;
    var resposta8B = document.getElementById("correta_8B").checked;
    var resposta9 = document.getElementById("correta_9").checked;
    var resposta10 = document.getElementById("correta_10").checked;

    var errado_7A = document.getElementById("errado_7A").checked;
    var errado_7B = document.getElementById("errado_7B").checked;
    var errado_7C = document.getElementById("errado_7C").checked;    
    var errado_8A = document.getElementById("errado_8A").checked;
    var errado_8B = document.getElementById("errado_8B").checked;

    var pontos = 0;

    var verifica_res_count1 = resposta1.length;
    var verifica_res1 = resposta1.substr(0, 3);

    var verifica_res2 = resposta2.length;
    var verifica_res3 = resposta3.indexOf("python manage.py runserver");

    if(verifica_res1.toUpperCase() == "SIM"){
        if((verifica_res_count1 - 3) > 10){
            pontos = pontos + 1;
        }        
    }
    if(verifica_res2 > 30){
        pontos = pontos + 1;
    }
    if(verifica_res3 > -1){
        pontos = pontos + 1;
    }
    if(resposta4 == true){
        pontos = pontos + 1;
    }
    if(resposta5 == true){
        pontos = pontos + 1;
    }
    if(resposta6 == true){
        pontos = pontos + 1;
    }
    if(resposta9 == true){
        pontos = pontos + 1;
    }
    if(resposta10 == true){
        pontos = pontos + 1;
    }
    
    if(resposta7 == true && errado_7A != true && errado_7B != true && errado_7C != true){
        pontos = pontos + 1;
    }

    if(resposta8A == true && resposta8B == true && errado_8A != true && errado_8B != true){
        pontos = pontos + 1;
    }


    if(pontos >= 5){
        alert("Aprovado!! Nota: "+pontos);
    }else{
        alert("Reprovado!! Estude Mais. Nota: "+pontos);
    }

    window.location.href = "/index.html";

}