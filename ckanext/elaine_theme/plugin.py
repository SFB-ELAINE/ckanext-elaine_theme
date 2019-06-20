import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def resolve_creator_user_id (creator_user_id):
    '''
    Return a dictionary of information about the user with the given creator_id

    :param creator_id: a user ID to resolve
    :type creator_id: string

    :returns: dictionary with details about the user
    :rtype: dictionary
    '''
    user_dict = toolkit.get_action('user_show')(None, data_dict={'id': creator_user_id})
    return user_dict

class ElaineThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # Declare that this plugin will implement ITemplateHelpers
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'elaine_theme')

    def get_helpers(self):
        '''
        Register resolve_creator_id() as a template helper function.
        '''
        return {'elaine_theme_resolve_creator_user_id': resolve_creator_user_id}
