"""
Script de verificación para confirmar que todos los métodos están correctamente definidos
"""

import ast
import inspect

def verify_todo_app_methods():
    """Verifica que todos los métodos necesarios estén definidos en TodoApp"""
    
    # Importar la clase TodoApp
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    from main import TodoApp
    
    # Métodos requeridos
    required_methods = [
        'show_notification',
        'hide_notification',
        'add_task',
        'update_task', 
        'delete_task',
        'cancel_delete_confirmation',
        'on_task_select',
        'load_tasks',
        'create_widgets',
        'calculate_days_left',
        'format_task_display'
    ]
    
    print("🔍 Verificando métodos de la clase TodoApp...")
    print("=" * 50)
    
    # Obtener todos los métodos de la clase
    class_methods = [method for method in dir(TodoApp) if not method.startswith('_')]
    
    missing_methods = []
    found_methods = []
    
    for method in required_methods:
        if hasattr(TodoApp, method):
            found_methods.append(method)
            print(f"✅ {method}")
        else:
            missing_methods.append(method)
            print(f"❌ {method} - NO ENCONTRADO")
    
    print("=" * 50)
    print(f"📊 Resumen:")
    print(f"✅ Métodos encontrados: {len(found_methods)}/{len(required_methods)}")
    print(f"❌ Métodos faltantes: {len(missing_methods)}")
    
    if missing_methods:
        print(f"\n🚨 Métodos faltantes:")
        for method in missing_methods:
            print(f"   - {method}")
        return False
    else:
        print("\n🎉 ¡Todos los métodos requeridos están presentes!")
        return True

def verify_notification_system():
    """Verifica que el sistema de notificaciones esté correctamente configurado"""
    print("\n🔔 Verificando sistema de notificaciones...")
    print("=" * 50)
    
    try:
        import tkinter as tk
        from main import TodoApp
        
        # Crear una instancia temporal (sin mostrar la ventana)
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana
        
        app = TodoApp(root)
        
        # Verificar que los atributos de notificación existen
        notification_attributes = [
            'notification_frame',
            'notification_label'
        ]
        
        for attr in notification_attributes:
            if hasattr(app, attr):
                print(f"✅ {attr}")
            else:
                print(f"❌ {attr} - NO ENCONTRADO")
                return False
        
        # Probar el método show_notification
        try:
            app.show_notification("Prueba", "success")
            print("✅ show_notification funciona correctamente")
        except Exception as e:
            print(f"❌ Error en show_notification: {e}")
            return False
        
        # Probar el método hide_notification
        try:
            app.hide_notification()
            print("✅ hide_notification funciona correctamente")
        except Exception as e:
            print(f"❌ Error en hide_notification: {e}")
            return False
        
        root.destroy()
        print("\n🎉 ¡Sistema de notificaciones verificado correctamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error al verificar sistema de notificaciones: {e}")
        return False

if __name__ == "__main__":
    print("🛠️  Verificación completa del sistema Py-To-Do")
    print("=" * 60)
    
    # Verificar métodos
    methods_ok = verify_todo_app_methods()
    
    # Verificar sistema de notificaciones
    notifications_ok = verify_notification_system()
    
    print("\n" + "=" * 60)
    if methods_ok and notifications_ok:
        print("🎉 ¡VERIFICACIÓN COMPLETADA EXITOSAMENTE!")
        print("✅ Todos los sistemas están funcionando correctamente")
        print("🚀 La aplicación está lista para usar")
    else:
        print("🚨 ¡VERIFICACIÓN FALLIDA!")
        print("❌ Hay problemas que necesitan ser corregidos")
    
    print("\n💡 Para probar la aplicación, ejecute: python main.py")
