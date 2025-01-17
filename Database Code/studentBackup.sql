PGDMP     4    2                {            student    15.1    15.1 .    1           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            2           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            3           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            4           1262    16776    student    DATABASE     z   CREATE DATABASE student WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
    DROP DATABASE student;
                postgres    false            �            1259    16792    course    TABLE     �   CREATE TABLE public.course (
    course_id integer NOT NULL,
    title character varying(100) NOT NULL,
    credits integer NOT NULL,
    department_id integer
);
    DROP TABLE public.course;
       public         heap    postgres    false            �            1259    16791    course_course_id_seq    SEQUENCE     �   CREATE SEQUENCE public.course_course_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.course_course_id_seq;
       public          postgres    false    219            5           0    0    course_course_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.course_course_id_seq OWNED BY public.course.course_id;
          public          postgres    false    218            �            1259    16785 
   department    TABLE     q   CREATE TABLE public.department (
    department_id integer NOT NULL,
    name character varying(100) NOT NULL
);
    DROP TABLE public.department;
       public         heap    postgres    false            �            1259    16784    department_department_id_seq    SEQUENCE     �   CREATE SEQUENCE public.department_department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.department_department_id_seq;
       public          postgres    false    217            6           0    0    department_department_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.department_department_id_seq OWNED BY public.department.department_id;
          public          postgres    false    216            �            1259    16815 
   enrollment    TABLE     �   CREATE TABLE public.enrollment (
    student_id integer NOT NULL,
    course_id integer NOT NULL,
    enrollment_date date NOT NULL,
    grade character(2)
);
    DROP TABLE public.enrollment;
       public         heap    postgres    false            �            1259    16804 	   professor    TABLE     �   CREATE TABLE public.professor (
    professor_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    department_id integer
);
    DROP TABLE public.professor;
       public         heap    postgres    false            �            1259    16803    professor_professor_id_seq    SEQUENCE     �   CREATE SEQUENCE public.professor_professor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.professor_professor_id_seq;
       public          postgres    false    221            7           0    0    professor_professor_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.professor_professor_id_seq OWNED BY public.professor.professor_id;
          public          postgres    false    220            �            1259    16778    student    TABLE     �   CREATE TABLE public.student (
    student_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    dob date NOT NULL,
    gender character(1) NOT NULL
);
    DROP TABLE public.student;
       public         heap    postgres    false            �            1259    16777    student_student_id_seq    SEQUENCE     �   CREATE SEQUENCE public.student_student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.student_student_id_seq;
       public          postgres    false    215            8           0    0    student_student_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.student_student_id_seq OWNED BY public.student.student_id;
          public          postgres    false    214            �            1259    16830    teaches    TABLE     �   CREATE TABLE public.teaches (
    professor_id integer NOT NULL,
    course_id integer NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL
);
    DROP TABLE public.teaches;
       public         heap    postgres    false            �            1259    16995    total    TABLE     W   CREATE TABLE public.total (
    title character varying(100),
    student_no bigint
);
    DROP TABLE public.total;
       public         heap    postgres    false            �           2604    16795    course course_id    DEFAULT     t   ALTER TABLE ONLY public.course ALTER COLUMN course_id SET DEFAULT nextval('public.course_course_id_seq'::regclass);
 ?   ALTER TABLE public.course ALTER COLUMN course_id DROP DEFAULT;
       public          postgres    false    218    219    219            �           2604    16788    department department_id    DEFAULT     �   ALTER TABLE ONLY public.department ALTER COLUMN department_id SET DEFAULT nextval('public.department_department_id_seq'::regclass);
 G   ALTER TABLE public.department ALTER COLUMN department_id DROP DEFAULT;
       public          postgres    false    217    216    217            �           2604    16807    professor professor_id    DEFAULT     �   ALTER TABLE ONLY public.professor ALTER COLUMN professor_id SET DEFAULT nextval('public.professor_professor_id_seq'::regclass);
 E   ALTER TABLE public.professor ALTER COLUMN professor_id DROP DEFAULT;
       public          postgres    false    220    221    221            �           2604    16781    student student_id    DEFAULT     x   ALTER TABLE ONLY public.student ALTER COLUMN student_id SET DEFAULT nextval('public.student_student_id_seq'::regclass);
 A   ALTER TABLE public.student ALTER COLUMN student_id DROP DEFAULT;
       public          postgres    false    214    215    215            )          0    16792    course 
   TABLE DATA           J   COPY public.course (course_id, title, credits, department_id) FROM stdin;
    public          postgres    false    219   95       '          0    16785 
   department 
   TABLE DATA           9   COPY public.department (department_id, name) FROM stdin;
    public          postgres    false    217   �5       ,          0    16815 
   enrollment 
   TABLE DATA           S   COPY public.enrollment (student_id, course_id, enrollment_date, grade) FROM stdin;
    public          postgres    false    222   �5       +          0    16804 	   professor 
   TABLE DATA           W   COPY public.professor (professor_id, first_name, last_name, department_id) FROM stdin;
    public          postgres    false    221   "6       %          0    16778    student 
   TABLE DATA           Q   COPY public.student (student_id, first_name, last_name, dob, gender) FROM stdin;
    public          postgres    false    215   p6       -          0    16830    teaches 
   TABLE DATA           P   COPY public.teaches (professor_id, course_id, start_date, end_date) FROM stdin;
    public          postgres    false    223   �6       .          0    16995    total 
   TABLE DATA           2   COPY public.total (title, student_no) FROM stdin;
    public          postgres    false    224   (7       9           0    0    course_course_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.course_course_id_seq', 3, true);
          public          postgres    false    218            :           0    0    department_department_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.department_department_id_seq', 3, true);
          public          postgres    false    216            ;           0    0    professor_professor_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.professor_professor_id_seq', 3, true);
          public          postgres    false    220            <           0    0    student_student_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.student_student_id_seq', 14, true);
          public          postgres    false    214            �           2606    16797    course course_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.course
    ADD CONSTRAINT course_pkey PRIMARY KEY (course_id);
 <   ALTER TABLE ONLY public.course DROP CONSTRAINT course_pkey;
       public            postgres    false    219            �           2606    16790    department department_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (department_id);
 D   ALTER TABLE ONLY public.department DROP CONSTRAINT department_pkey;
       public            postgres    false    217            �           2606    16819    enrollment enrollment_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.enrollment
    ADD CONSTRAINT enrollment_pkey PRIMARY KEY (student_id, course_id);
 D   ALTER TABLE ONLY public.enrollment DROP CONSTRAINT enrollment_pkey;
       public            postgres    false    222    222            �           2606    16809    professor professor_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_pkey PRIMARY KEY (professor_id);
 B   ALTER TABLE ONLY public.professor DROP CONSTRAINT professor_pkey;
       public            postgres    false    221            �           2606    16783    student student_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (student_id);
 >   ALTER TABLE ONLY public.student DROP CONSTRAINT student_pkey;
       public            postgres    false    215            �           2606    16834    teaches teaches_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public.teaches
    ADD CONSTRAINT teaches_pkey PRIMARY KEY (professor_id, course_id);
 >   ALTER TABLE ONLY public.teaches DROP CONSTRAINT teaches_pkey;
       public            postgres    false    223    223            �           2606    16798     course course_department_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.course
    ADD CONSTRAINT course_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.department(department_id);
 J   ALTER TABLE ONLY public.course DROP CONSTRAINT course_department_id_fkey;
       public          postgres    false    217    3207    219            �           2606    16825 $   enrollment enrollment_course_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.enrollment
    ADD CONSTRAINT enrollment_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.course(course_id);
 N   ALTER TABLE ONLY public.enrollment DROP CONSTRAINT enrollment_course_id_fkey;
       public          postgres    false    222    219    3209            �           2606    16820 %   enrollment enrollment_student_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.enrollment
    ADD CONSTRAINT enrollment_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student(student_id);
 O   ALTER TABLE ONLY public.enrollment DROP CONSTRAINT enrollment_student_id_fkey;
       public          postgres    false    222    215    3205            �           2606    16810 &   professor professor_department_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.department(department_id);
 P   ALTER TABLE ONLY public.professor DROP CONSTRAINT professor_department_id_fkey;
       public          postgres    false    217    221    3207            �           2606    16840    teaches teaches_course_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.teaches
    ADD CONSTRAINT teaches_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.course(course_id);
 H   ALTER TABLE ONLY public.teaches DROP CONSTRAINT teaches_course_id_fkey;
       public          postgres    false    219    3209    223            �           2606    16835 !   teaches teaches_professor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.teaches
    ADD CONSTRAINT teaches_professor_id_fkey FOREIGN KEY (professor_id) REFERENCES public.professor(professor_id);
 K   ALTER TABLE ONLY public.teaches DROP CONSTRAINT teaches_professor_id_fkey;
       public          postgres    false    221    3211    223            )   Q   x�3�LI,ILJ,NU�,.I��4�4�2����KM,Rp�IOM*J�4�4�2�t�I,.�LN�Q�MM�H��L.*7����� C/      '   1   x�3�t��-(-I-R(N�L�KN�2��u,��2�Ȩ,�L.����� �      ,   7   x�3�4�4202�5 !NG.#N#d'.cNcdg.C�#]K ������ ���      +   >   x�3��������+���4�2�N,J�,��,��4�2����N�����L�-�4����� ���      %   o   x�3��J�K���,��4��4�50�52�t�2�t�O�����+���4200�5��5����2��K,J-���.�M,i3�50"��1gAQf^r*g6X�(i�h�G2F��� :1#D      -   )   x�3�4�4202�5 !(�T�ؐˈ���1�1�=... @M�      .      x������ � �     