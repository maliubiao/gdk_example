#include <stdlib.h>
#include <gtk/gtk.h>
void key_press_action(GtkWidget *widget, GdkEvent *event,gpointer user_data);
void quit_application(void);
int main(int argc, char** argv)
{
	gtk_init(&argc,&argv);
	GtkWidget *window; 
	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	g_signal_connect(window, "delete-event", quit_application,NULL);
	g_signal_connect(window, "key-press-event",key_press_action,NULL);
	gtk_widget_show(window);
	gtk_main();
}
void key_press_action(GtkWidget *widget, GdkEvent *event,gpointer user_data)
{
	GdkEventKey *ke = (GdkEventKey *)event;
	gchar keyname[32];
	g_strlcpy(keyname,gdk_keyval_name(ke->keyval),sizeof(keyname));
	if(!g_strcmp0(keyname,"p"))
	{
		//paint
		//
		
	}
}
void quit_application(void)
{

	gtk_main_quit();
	_exit(0);
}
