var tempoInicial = $("#tempo-digitacao").text();
var campo = $(".campo-digitacao");

$(document).ready(function(){
    Contador();
    Cronometro();
    mudaBorda();
    inserePlacar();    finalGame();
    $("#reiniciar").on("click", ReiniciarGame)
});



function Contador(){
    var frase = $(".frase").text();
    var numPalavras = frase.split(" ").length;

    var tamanhoFrase = $("#tamanho-frase");
    tamanhoFrase.text(numPalavras);

    var campo = $(".campo-digitacao");
    campo.on("input", function() {
        var conteudo = campo.val();
    
        var qtdPalavras = conteudo.split(/\S+/).length - 1;
        $("#contador-palavras").text(qtdPalavras);
    
        var qtdCaracteres = conteudo.length;
        $("#contador-caracteres").text(qtdCaracteres);
    });
}
campo.on("input", function() {
    var conteudo = campo.val();

    var qtdPalavras = conteudo.split(/\S+/).length - 1;
    $("#contador-palavras").text(qtdPalavras);

    var qtdCaracteres = conteudo.length;
    $("#contador-caracteres").text(qtdCaracteres);
});

function Cronometro(){
    var tempoRestante = $("#tempo-digitacao").text();
    campo.one("focus", function() {
        $("#reiniciar").attr("disabled", false);
        var cronometroID = setInterval(function() {
            tempoRestante--;
            $("#tempo-digitacao").text(tempoRestante);
            if (tempoRestante < 1) {
                clearInterval(cronometroID);
                
                finalGame();
            }
        }, 1000);
    });
}

function finalGame(){
    campo.attr("disabled", true );
    $("#reiniciar").attr("disabled", true);
    campo.addClass("campo-desativado");
    inserePlacar();


}

function mudaBorda(){ 
var frase = $(".frase").text();
campo.on("input", function(){
    var digitacao = campo.val();
    var comparavel = frase.substring(0, digitacao.length);
    
    if (digitacao == comparavel){
        campo.addClass("borda-verde");
        campo.removeClass("borda-vermelha");
    }else{
        campo.addClass("borda-vermelha");
        campo.removeClass("borda-verde")
    }
});}

function inserePlacar(){
    var corpoTabela = $(".placar").find("tbody");
    var usuario = "joedson";
    var numeroPalavras = $("#contador-palavras").text();

    var linha = "<tr>"+
                "<td>"+usuario+"</td>"+
                "<td>"+numeroPalavras+"</td>"+
                "</tr>";
        
    corpoTabela.prepend(linha);
}

function ReiniciarGame(){
  
    campo.attr("disabled", false);
    campo.val("");
    $("#contador-palavras").text("0");
    $("#contador-caracteres").text("0");
    $("#tempo-digitacao").text(tempoInicial);
    Cronometro();
    campo.removeClass("campo-desativado")
    campo.removeClass("borda-verde");
    campo.removeClass("borda-vermelha");   
}
