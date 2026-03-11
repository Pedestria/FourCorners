package pedestria.fourcorners;

import pedestria.fourcorners.client.gui.GuiHandler;
import pedestria.fourcorners.init.InitRecipes;
import pedestria.fourcorners.proxy.CommonProxy;
import pedestria.fourcorners.util.FourCornersTab;
import pedestria.fourcorners.util.Reference;
import net.minecraft.creativetab.CreativeTabs;
//import pedestria.fourcorners.world.MainWorldGenerator;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventHandler;
import net.minecraftforge.fml.common.Mod.Instance;
import net.minecraftforge.fml.common.SidedProxy;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPostInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;
import net.minecraftforge.fml.common.network.NetworkRegistry;
//import net.minecraftforge.fml.common.registry.GameRegistry;

/*
 * This class is setting up the proxys and the main initialization stages.
 * The first line is defining that this is the main class that the program will run in.
 * (@Mod())
 * After that I'm declaring the class as an instance and I am defining it as an object called "main"
 * Then the two different proxys are declared here.
 * and then the three big stages.
 * 
 * The first stage is the Pre-Intialization stage. Basically this is the setup command of the program.
 * The second stage is the Initialization stage, where the main blocks and items are registered.
 * The final stage is the Post-Initialization, where last minute events and objects are declared.
 * 
 */

@Mod (modid = Reference.MODID,name = Reference.NAME,version = Reference.VERSION)
public class FourCorners {
	@Instance
	public static FourCorners main;
	
	//Setting up the proxys on both the client and the server.
	@SidedProxy(clientSide = Reference.CLIENT_PROXY_CLASS,serverSide = Reference.COMMON_PROXY_CLASS)
	public static CommonProxy proxy;
	
	public static CreativeTabs fcTab = new FourCornersTab();
	
	public FourCorners () 
	{
		//GameRegistry.registerWorldGenerator(new MainWorldGenerator(), 0);
	}
	
	//This is the first stage of loading.
	@EventHandler
	public void preInit (FMLPreInitializationEvent event) {
		proxy.registerOreDict();
		CommonProxy.initTileEntities();
		
		
	}
	//This is the second stage of loading.
	@EventHandler
	public void init (FMLInitializationEvent event) {
		InitRecipes.init();
		NetworkRegistry.INSTANCE.registerGuiHandler(main, new GuiHandler());
		
		
	}
	//This is the third and final stage of loading.
	@EventHandler
	public void postInit (FMLPostInitializationEvent event) {
		
	}
}
