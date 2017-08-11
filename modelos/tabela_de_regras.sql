--CREATE TABLE public.layer_rules ("camada" text, "tipo_regra" text, "descricao" text, "cor_rgb" text, "regra" text, "tipo_estilo" text);

INSERT INTO public.layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo) 
VALUES ('Trecho_Drenagem_L', 'linha', 'teste 2', '88,214,141', 'left(lower("nome"), 3) is ''rio''', 'aquisicao');

INSERT INTO public.layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo) 
VALUES ('Trecho_Rodoviario_L', 'campo', 'teste 3', '165,105,189', '"nrFaixas" is 1', 'aquisicao');

--INSERT INTO public.layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo) 
--VALUES ("", "", "", "", "","")
