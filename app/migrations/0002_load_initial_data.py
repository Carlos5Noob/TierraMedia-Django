from django.db import migrations

def poblar_armas(apps, schema_editor):
    Arma = apps.get_model('app', 'Arma')
    Arma.objects.create(nombre= 'Hacha doble',dano= 40, critico=40)
    Arma.objects.create(nombre= 'Andúril',dano= 60, critico=10)
    Arma.objects.create(nombre= 'Dagas de los Túmulos',dano= 30, critico=60)
    Arma.objects.create(nombre= 'Narsil',dano= 70, critico=7)
    Arma.objects.create(nombre= 'Flecha negra',dano= 20, critico=100)

def poblar_facciones(apps, schema_editor):
    Faccion = apps.get_model('app', 'Faccion')
    Faccion.objects.create(nombre='Hombres del Oeste', descripcion='Valientes y nobles, los Hombres del Oeste luchan por la libertad y la justicia en los confines de la tierra. Enfrentan un mundo en constante peligro, pero su determinación es inquebrantable.')
    Faccion.objects.create(nombre='Elfos', descripcion='Seres etéreos y sabios, los Elfos poseen una conexión profunda con la naturaleza y la magia antigua. A lo largo de los siglos, han mantenido su elegancia y gracia, pero no son ajenos a la lucha por la supervivencia.')
    Faccion.objects.create(nombre='Enanos', descripcion='Rudos y resistentes, los Enanos habitan las montañas y las profundidades de la tierra. Son artesanos inigualables y guerreros ferozmente leales, siempre dispuestos a defender su hogar y su honor.')
    Faccion.objects.create(nombre='Mordor', descripcion='Tierra de sombras y maldad, Mordor es el hogar de aquellos que sirven a la oscuridad. Con su ominoso líder, Sauron, esta región está marcada por la desesperación y el terror, y sus seguidores buscan conquistar todo lo que tocan.')
    Faccion.objects.create(nombre='Trasgos', descripcion='Criaturas repulsivas y astutas, los Trasgos habitan las cavernas oscuras y las tierras infértiles. A menudo serviles y caóticos, su naturaleza destructiva los convierte en una amenaza constante para sus enemigos.')
    Faccion.objects.create(nombre='Isengard', descripcion='Isengard, una fortaleza de acero y oscuridad, es gobernada por Saruman, el mago caído. Con sus huestes de orcos y máquinas de guerra, busca dominar la tierra, imbuido por su deseo de poder absoluto.')

def poblar_ubicaciones(apps, schema_editor):
    Ubicacion = apps.get_model('app', 'Ubicacion')
    Ubicacion.objects.create(nombre='Rivendel', descripcion='Un refugio sereno y lleno de sabiduría, Rivendel es un paraíso escondido entre las montañas. Los Elfos han vivido aquí por siglos, preservando su cultura y magia mientras ofrecen hospitalidad a los viajeros que buscan paz.')
    Ubicacion.objects.create(nombre='Minas Tirith', descripcion='La majestuosa capital de Gondor, Minas Tirith se alza como una fortaleza de blanca piedra sobre las colinas. Es el símbolo de la resistencia humana ante el mal, un bastión de coraje y esperanza en tiempos de guerra.')
    Ubicacion.objects.create(nombre='La Comarca', descripcion='Un lugar tranquilo y lleno de verdes praderas, La Comarca es el hogar de los Hobbits. Aquí, la vida sigue su curso pacífico, alejado de las grandes batallas, donde el tiempo parece no correr y la naturaleza se disfruta sin prisas.')
    Ubicacion.objects.create(nombre='Mordor', descripcion='Un reino oscuro y desolado, Mordor es la tierra gobernada por Sauron. Su paisaje árido y cubierto de cenizas está marcado por el dominio de la oscuridad, donde solo se ve la huella de la opresión y la guerra interminable.')
    Ubicacion.objects.create(nombre='Bosque Negro', descripcion='Un bosque antiguo y misterioso, donde las sombras acechan y las criaturas oscuras se esconden entre los árboles. Pocos se atreven a aventurarse aquí, ya que el Bosque Negro guarda secretos que podrían llevar a cualquiera a la perdición.')
    Ubicacion.objects.create(nombre='Isengard', descripcion='Una fortaleza de imponentes torres y maquinaria de guerra, Isengard es el hogar de Saruman, un mago que se ha dejado consumir por su ansia de poder. Rodeada de un vasto campo industrial, esta tierra se ha convertido en un centro de fabricación de terror y destrucción.')

def poblar_personajes(apps, schema_editor):
    Personaje = apps.get_model('app', 'Personaje')
    Faccion = apps.get_model('app', 'Faccion')
    Ubicacion = apps.get_model('app', 'Ubicacion')
    Arma = apps.get_model('app', 'Arma')

    # Creamos las facciones
    hombres_del_oeste = Faccion.objects.create(nombre='Hombres del Oeste', descripcion='Hombres nobles y valientes.')
    elfos = Faccion.objects.create(nombre='Elfos', descripcion='Seres longevos y sabios de los bosques y montañas.')
    # Creamos las ubicaciones
    minas_tirith = Ubicacion.objects.create(nombre='Minas Tirith', descripcion='La majestuosa ciudad de los hombres, capital de Gondor.')
    rivendel = Ubicacion.objects.create(nombre='Rivendel', descripcion='La casa de los Elfos, un refugio de sabiduría y belleza.')
    # Creamos las armas
    anduril = Arma.objects.create(nombre='Andúril', dano=60, critico=10)
    flecha_negra = Arma.objects.create(nombre='Flecha negra', dano=20, critico=100)


    # Creamos los personajes
    Personaje.objects.create(
        nombre='Aragorn',
        salud=120,
        mana=50,
        arma=anduril,
        faccion=hombres_del_oeste,
        ubicacion=minas_tirith,
        foto='aragorn.jpg'
    )

    Personaje.objects.create(
        nombre='Legolas',
        salud=100,
        mana=70,
        arma=flecha_negra,
        faccion=elfos,
        ubicacion=rivendel,
        foto='legolas.jpg'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(poblar_armas),
        migrations.RunPython(poblar_facciones),
        migrations.RunPython(poblar_ubicaciones),
        migrations.RunPython(poblar_personajes),
    ]