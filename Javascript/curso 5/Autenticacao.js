export class Autenticacao {

    // Métodos estáticos ------------------------------------------------------------
    
    static login(autenticavel, senha) {

        if(!Autenticacao.ehAutenticavel) {
            
            return false;
        }

        return autenticavel.autenticar(senha);
    }

    static ehAutenticavel(autenticavel) {

        return "autenticar" in autenticavel &&
                autenticavel.autenticar instanceof Function;
    }
}