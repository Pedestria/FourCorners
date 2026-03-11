package pedestria.fourcorners.blocks;


import java.util.Random;

import net.minecraft.block.SoundType;
import net.minecraft.block.material.Material;
import net.minecraft.item.Item;

public class WisdomOreBlock extends ItemDropOreBlock {

	
	public WisdomOreBlock(String name, Material material, Item toDrop) {
		super(name,material,toDrop);
		
		setSoundType(SoundType.METAL);
		setHardness(4.0F);
		setResistance(35.0F);
		setHarvestLevel("pickaxe", 3);
		setLightLevel(11.0F);
	}
	
	@Override
	public int quantityDropped(Random random) {

		int min = 1;
		int max = 3;
		return random.nextInt(max) + min;
	}
}
