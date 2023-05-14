create table movies
(
    id       serial not null
        constraint movies_pk
            primary key,
    title    varchar(250),
    duration smallint,
    released date
);

alter table movies
    owner to ppl;

create unique index movies_id_uindex
    on movies (id);


select * from movies;