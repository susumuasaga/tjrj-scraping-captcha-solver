/*  Tribunal de Justiça do Estado do Rio de Janeiro
    Autor: Felipe Ribeiro Santos
    Histórico:
        @@@ v2.0.0 - 02/04/2012

*/

function getXMLHttpRequest(){
    if (window.XMLHttpRequest) {
        return new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        return new ActiveXObject("Microsoft.XMLHTTP");
    }
}

function gerarNovaImagem(){
    var url = "./captcha";
    req = getXMLHttpRequest();
    req.open("GET",url,true);
    req.onreadystatechange = callback;
    req.send(null);
}

function callback(){
    if(req.readyState==4){
        if(req.status == 200){
            var imagem = document.getElementById('imgCaptcha');
            imagem.src = "./captcha?" + Math.random();
        }
    }
    apagarFormulario();
    focarEm();
}

function apagarFormulario(){
    document.forms[0].reset();
}

function focarEm(){
    document.getElementById("captcha").focus();
}

function validarCampos(){

    retorno = true;

    var captcha = document.forms['unicoForm'].captcha.value;
        if(!(captcha != '' && captcha.length > 0)){
            alert('O Código de Segurança deve ser informado.');
            retorno = false;
        }
    return retorno;
}

function submeter(){
    if(validarCampos()){
        document.forms[0].submit();
    }
}

function inicializaModoAudio(){
    document.getElementById('img_container').className = "invisivel";
    document.getElementById('sound_container').className = "visivel";

    document.getElementById('sp_modoAudio').className = "invisivel";
    document.getElementById('sp_modoImagem').className = "visivel";
    play();
}

function inicializaModoImagem(){
    document.getElementById('img_container').className = "visivel";
    document.getElementById('sound_container').className = "invisivel";

    document.getElementById('sp_modoImagem').className = "invisivel";
    document.getElementById('sp_modoAudio').className = "visivel";

    stop();
    gerarNovaImagem();
}

function play(){
    _audiocaptcha = $('#deck_player');
    _audiocaptcha.flash(
                {
                        swf: 'audio.wav',
                        width: 1,
                        height: 1,
                        loop: false,
			autoplay:false
                }
    );
}

function replay() {
    _audiocaptcha = $('#deck_player');
    _audiocaptcha.flash(
            function() {
                    this.Play();
            }
    );
}

function stop() {
    _audiocaptcha = $('#deck_player');
    _audiocaptcha.flash(
            function() {
                    this.StopPlay();
            }
    );
}