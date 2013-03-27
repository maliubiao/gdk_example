#include <stdlib.h>
#include <gdk/gdk.h>

void delete_window_handler(GdkWindow *window, GdkEvent *event, gpointer user_data);
int main(int argc, char **argv)
{
	gdk_init(&argc,&argv);
	//create a GdkWidnow
	GdkWindowAttr *gwa = malloc(sizeof(GdkWindowAttr));
	gwa->title="hello world";
	gwa->event_mask=GDK_ALL_EVENTS_MASK;
	gwa->x=0;
	gwa->y=0;
	gwa->width=800;
	gwa->height=800;
	gwa->wclass=GDK_INPUT_OUTPUT;
	gwa->visual=gdk_visual_get_best();
	gwa->window_type=GDK_WINDOW_TOPLEVEL;
	gwa->cursor=gdk_cursor_new(GDK_ARROW);
	gwa->wmclass_name=NULL;
	gwa->wmclass_class=NULL;
	gwa->override_redirect=0;
	gwa->type_hint=GDK_WINDOW_TYPE_HINT_NORMAL;
	GdkWindow *window;	
	window=gdk_window_new(NULL,gwa,GDK_WA_TITLE|GDK_WA_X|GDK_WA_Y );
	gdk_window_show(window);

	GdkEvent *event; 
	while(1)
	{
		event = gdk_event_get();
		if(event == NULL)
			continue;
		switch(event->type)
		{
			case GDK_DELETE:
				{
					delete_window_handler(window,event,NULL);
					break; 
				}
			case GDK_MOTION_NOTIFY:
				break;
			case GDK_BUTTON_PRESS:
				break;
			case GDK_KEY_PRESS:
				break;
			default:
				break;
		}
	}
	_exit(0);
}
void delete_window_handler(GdkWindow *window, GdkEvent *event, gpointer user_data)
{
	gdk_window_destroy(window);
	_exit(0);
}
