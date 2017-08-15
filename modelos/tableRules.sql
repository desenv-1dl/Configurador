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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: layer_rules; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE layer_rules (
    camada text,
    tipo_regra text,
    nome text,
    cor_rgb text,
    regra text,
    tipo_estilo text,
    atributo text,
    descricao text
);


ALTER TABLE layer_rules OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

