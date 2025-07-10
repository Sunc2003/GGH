from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from models import Usuario, Rol, Area, Cargo

@receiver(post_migrate)
def crear_usuario_base(sender, **kwargs):
    correo = "gneira@ggh.cl"
    if not Usuario.objects.filter(correo=correo).exists():
        # Busca o crea los valores necesarios
        rol_admin, _ = Rol.objects.get_or_create(nombre_rol="Administrador", defaults={"descripcion": "Rol por defecto"})
        area_general, _ = Area.objects.get_or_create(nombre_area="Sistemas", defaults={"descripcion": "Área general"})
        cargo_admin, _ = Cargo.objects.get_or_create(nombre_cargo="Administrador", defaults={"descripcion": "Encargado responsable del area de TI"})

        # Crear el usuario
        Usuario.objects.create(
            nombre="Gonzalo",
            apellido="Neira",
            correo=correo,
            contraseña="2025",  # Deberías encriptarla si usarás login real
            direccion="Oficina Central",
            telefono="123456789",
            id_area=area_general,
            id_cargo=cargo_admin,
            id_rol=rol_admin
        )

        print("✅ Usuario administrador creado correctamente.")
    else:
        print("ℹ️ El usuario ya existe.")