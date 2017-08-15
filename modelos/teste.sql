--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- Data for Name: layer_rules; Type: TABLE DATA; Schema: public; Owner: user
--

CREATE TABLE public.layer_rules ("camada" text, "tipo_regra" text, "nome" text, "descricao" text, "cor_rgb" text, "regra" text, "tipo_estilo" text, "atributo" text);

INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_a', 'Atributo', 'tipo_delimitacao deve ser Não aplicável (97)', '231,76,60', '"tipo_delimitacao" != 97', 'Aquisição', 'tipo_delimitacao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_a', 'Atributo', 'tipo não dever ser (1), (2) ou (3)', '231,76,60', '"tipo" IN (1,2,3)', 'Aquisição', 'tipo');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_a', 'Atributo', 'nome: verificar espaços e iniciar com maiúsculo', '231,76,60', 'regexp_match( "nome" , ''^ ''  ) or  regexp_match( "nome" , ''  ''  ) or  regexp_match( "nome" , '' $''  ) or  regexp_match( "nome" , ''^[a-z]''  )', 'Aquisição', 'nome');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_a', 'Atributo', 'preencher geometria_aproximada', '243,156,18', '"geometria_aproximada" = 999', 'Aquisição', 'geometria_aproximada');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_a', 'Atributo', 'preencher tipo_delimitacao', '243,156,18', '"tipo_delimitacao" = 999', 'Aquisição', 'tipo_delimitacao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_l', 'Atributo', 'tipo_delimitacao não deve ser Não aplicável (97)', '231,76,60', '"tipo_delimitacao" = 97', 'Aquisição', 'tipo_delimitacao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_l', 'Atributo', 'Os valores válidos para tipo são (1), (2) ou (3)', '231,76,60', '"tipo" NOT IN (1,2,3)', 'Aquisição', 'tipo');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_l', 'Atributo', 'nome: verificar espaços e iniciar com maiúsculo', '231,76,60', 'regexp_match( "nome" , ''^ ''  ) or  regexp_match( "nome" , ''  ''  ) or  regexp_match( "nome" , '' $''  ) or  regexp_match( "nome" , ''^[a-z]''  )', 'Aquisição', 'nome');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_l', 'Atributo', 'preencher geometria_aproximada', '243,156,18', '"geometria_aproximada" = 999', 'Aquisição', 'geometria_aproximada');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_legal_l', 'Atributo', 'preencher tipo_delimitacao', '243,156,18', '"tipo_delimitacao" = 999', 'Aquisição', 'tipo_delimitacao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_a', 'Atributo', 'tipo_delimitacao deve ser Não aplicável (97)', '231,76,60', '"tipo_delimitacao" != 97', 'Aquisição', 'tipo_delimitacao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_a', 'Atributo', 'nome: verificar espaços e iniciar com maiúsculo', '231,76,60', 'regexp_match( "nome" , ''^ ''  ) or  regexp_match( "nome" , ''  ''  ) or  regexp_match( "nome" , '' $''  ) or  regexp_match( "nome" , ''^[a-z]''  )', 'Aquisição', 'nome');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_a', 'Atributo', 'preencher geometria_aproximada', '243,156,18', '"geometria_aproximada" = 999', 'Aquisição', 'geometria_aproximada');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_a', 'Atributo', 'preencher tipo', '243,156,18', '"tipo" = 999', 'Reambulação', 'tipo');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_a', 'Atributo', 'preencher tipo_delimitacao', '243,156,18', '"tipo_delimitacao" = 999', 'Reambulação', 'tipo_delimitacao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_l', 'Atributo', 'tipo_delimitacao não deve ser Não aplicável (97)', '231,76,60', '"tipo_delimitacao" = 97', 'Aquisição', 'tipo_delimitacao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_l', 'Atributo', 'nome: verificar espaços e iniciar com maiúsculo', '231,76,60', 'regexp_match( "nome" , ''^ ''  ) or  regexp_match( "nome" , ''  ''  ) or  regexp_match( "nome" , '' $''  ) or  regexp_match( "nome" , ''^[a-z]''  )', 'Aquisição', 'nome');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_l', 'Atributo', 'preencher geometria_aproximada', '243,156,18', '"geometria_aproximada" = 999', 'Aquisição', 'geometria_aproximada');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_l', 'Atributo', 'preencher tipo', '243,156,18', '"tipo" = 999', 'Reambulação', 'tipo');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('limite_especial_l', 'Atributo', 'preencher tipo_delimitacao', '243,156,18', '"tipo_delimitacao" = 999', 'Reambulação', 'tipo_delimitacao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('delimitacao_fisica_l', 'Atributo', 'Muro é incomum para tipo, verificar', '247,220,111', '"tipo" = 2', 'Aquisição', 'tipo');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('delimitacao_fisica_l', 'Atributo', 'Materiais de construção invalidos para Cerca', '231,76,60', '"tipo" = 1 AND "material_construcao" IN (1,4)', 'Aquisição', 'material_construcao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('delimitacao_fisica_l', 'Atributo', 'Materiais de construção invalidos para Muro', '231,76,60', '"tipo" = 1 AND "material_construcao" IN (6,7,8)', 'Aquisição', 'material_construcao');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('delimitacao_fisica_l', 'Atributo', 'preencher tipo', '243,156,18', '"tipo" = 999', 'Reambulação', 'tipo');
INSERT INTO layer_rules (camada, tipo_regra, descricao, cor_rgb, regra, tipo_estilo, atributo) VALUES ('delimitacao_fisica_l', 'Atributo', 'preencher material_construcao', '243,156,18', '"material_construcao" IN (0,999)', 'Reambulação', 'material_construcao');


--
-- PostgreSQL database dump complete
--

