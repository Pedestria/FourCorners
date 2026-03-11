package pedestria.fourcorners.init;

import net.minecraft.item.ItemStack;
import net.minecraftforge.fml.common.registry.GameRegistry;

public class InitRecipes {
	
	public static void init () 
	{
		//Item Registry
		GameRegistry.addSmelting(InitItems.AVALON_GEM, new ItemStack(InitItems.AVALON_INGOT), 4);
		GameRegistry.addSmelting(InitItems.WISDOM_SHARD, new ItemStack(InitItems.WISDOM_INGOT), 11);
		
	}
}
